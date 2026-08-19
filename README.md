# SyndProxy private pool

## Current pool

- Alive now: 1286
- Gold now: 410
- HTTP: 450 alive / 97 gold
- HTTPS: 290 alive / 17 gold
- SOCKS4: 239 alive / 141 gold
- SOCKS5: 307 alive / 155 gold

## Historical pool

- Discovered: 131826
- Ever alive: 20987
- Ever gold: 877

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
