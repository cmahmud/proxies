# SyndProxy private pool

## Current pool

- Alive now: 918
- Gold now: 398
- HTTP: 284 alive / 96 gold
- HTTPS: 190 alive / 31 gold
- SOCKS4: 226 alive / 141 gold
- SOCKS5: 218 alive / 130 gold

## Historical pool

- Discovered: 163255
- Ever alive: 31772
- Ever gold: 1166

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
