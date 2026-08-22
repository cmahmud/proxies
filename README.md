# SyndProxy private pool

## Current pool

- Alive now: 1015
- Gold now: 428
- HTTP: 321 alive / 95 gold
- HTTPS: 230 alive / 34 gold
- SOCKS4: 187 alive / 127 gold
- SOCKS5: 277 alive / 172 gold

## Historical pool

- Discovered: 161919
- Ever alive: 31145
- Ever gold: 1155

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
