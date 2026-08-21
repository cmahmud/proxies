# SyndProxy private pool

## Current pool

- Alive now: 1019
- Gold now: 443
- HTTP: 325 alive / 105 gold
- HTTPS: 225 alive / 29 gold
- SOCKS4: 211 alive / 151 gold
- SOCKS5: 258 alive / 158 gold

## Historical pool

- Discovered: 153726
- Ever alive: 28580
- Ever gold: 1110

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
