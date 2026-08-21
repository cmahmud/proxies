# SyndProxy private pool

## Current pool

- Alive now: 844
- Gold now: 427
- HTTP: 246 alive / 90 gold
- HTTPS: 165 alive / 20 gold
- SOCKS4: 210 alive / 163 gold
- SOCKS5: 223 alive / 154 gold

## Historical pool

- Discovered: 152161
- Ever alive: 27850
- Ever gold: 1103

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
