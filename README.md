# SyndProxy validated proxy pool

## Current pool

- Alive now: 646
- Gold now: 447
- HTTP: 127 alive / 84 gold
- HTTPS: 136 alive / 31 gold
- SOCKS4: 172 alive / 161 gold
- SOCKS5: 211 alive / 171 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46612
- Ever gold: 1445

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
