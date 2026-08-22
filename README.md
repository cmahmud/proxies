# SyndProxy private pool

## Current pool

- Alive now: 908
- Gold now: 392
- HTTP: 265 alive / 83 gold
- HTTPS: 189 alive / 26 gold
- SOCKS4: 212 alive / 137 gold
- SOCKS5: 242 alive / 146 gold

## Historical pool

- Discovered: 163863
- Ever alive: 31972
- Ever gold: 1170

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
