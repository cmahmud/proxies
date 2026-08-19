# SyndProxy private pool

## Current pool

- Alive now: 1155
- Gold now: 521
- HTTP: 425 alive / 154 gold
- HTTPS: 268 alive / 93 gold
- SOCKS4: 248 alive / 148 gold
- SOCKS5: 214 alive / 126 gold

## Historical pool

- Discovered: 123176
- Ever alive: 18917
- Ever gold: 730

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
