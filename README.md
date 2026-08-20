# SyndProxy private pool

## Current pool

- Alive now: 1026
- Gold now: 424
- HTTP: 329 alive / 97 gold
- HTTPS: 217 alive / 24 gold
- SOCKS4: 228 alive / 151 gold
- SOCKS5: 252 alive / 152 gold

## Historical pool

- Discovered: 144747
- Ever alive: 25173
- Ever gold: 1056

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
