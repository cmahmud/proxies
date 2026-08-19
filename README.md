# SyndProxy private pool

## Current pool

- Alive now: 1181
- Gold now: 529
- HTTP: 429 alive / 152 gold
- HTTPS: 328 alive / 106 gold
- SOCKS4: 225 alive / 143 gold
- SOCKS5: 199 alive / 128 gold

## Historical pool

- Discovered: 127372
- Ever alive: 19945
- Ever gold: 804

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
