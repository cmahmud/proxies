# SyndProxy private pool

## Current pool

- Alive now: 1242
- Gold now: 406
- HTTP: 421 alive / 94 gold
- HTTPS: 278 alive / 17 gold
- SOCKS4: 239 alive / 140 gold
- SOCKS5: 304 alive / 155 gold

## Historical pool

- Discovered: 131826
- Ever alive: 20987
- Ever gold: 877

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
