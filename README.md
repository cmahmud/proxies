# SyndProxy validated proxy pool

## Current pool

- Alive now: 652
- Gold now: 472
- HTTP: 147 alive / 95 gold
- HTTPS: 127 alive / 41 gold
- SOCKS4: 181 alive / 163 gold
- SOCKS5: 197 alive / 173 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46936
- Ever gold: 1457

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
