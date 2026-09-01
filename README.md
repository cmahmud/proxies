# SyndProxy validated proxy pool

## Current pool

- Alive now: 644
- Gold now: 448
- HTTP: 126 alive / 85 gold
- HTTPS: 136 alive / 31 gold
- SOCKS4: 173 alive / 161 gold
- SOCKS5: 209 alive / 171 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46612
- Ever gold: 1445

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
