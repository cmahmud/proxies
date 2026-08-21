# SyndProxy private pool

## Current pool

- Alive now: 867
- Gold now: 395
- HTTP: 226 alive / 79 gold
- HTTPS: 171 alive / 21 gold
- SOCKS4: 243 alive / 158 gold
- SOCKS5: 227 alive / 137 gold

## Historical pool

- Discovered: 156830
- Ever alive: 29623
- Ever gold: 1133

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
