# SyndProxy private pool

## Current pool

- Alive now: 1208
- Gold now: 402
- HTTP: 393 alive / 93 gold
- HTTPS: 278 alive / 15 gold
- SOCKS4: 235 alive / 140 gold
- SOCKS5: 302 alive / 154 gold

## Historical pool

- Discovered: 131826
- Ever alive: 20987
- Ever gold: 877

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
