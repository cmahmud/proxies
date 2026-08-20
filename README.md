# SyndProxy private pool

## Current pool

- Alive now: 902
- Gold now: 392
- HTTP: 265 alive / 82 gold
- HTTPS: 197 alive / 25 gold
- SOCKS4: 220 alive / 142 gold
- SOCKS5: 220 alive / 143 gold

## Historical pool

- Discovered: 151072
- Ever alive: 27471
- Ever gold: 1097

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
