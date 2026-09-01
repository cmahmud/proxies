# SyndProxy validated proxy pool

## Current pool

- Alive now: 644
- Gold now: 447
- HTTP: 125 alive / 84 gold
- HTTPS: 127 alive / 30 gold
- SOCKS4: 175 alive / 161 gold
- SOCKS5: 217 alive / 172 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46605
- Ever gold: 1445

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
