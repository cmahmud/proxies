# SyndProxy private pool

## Current pool

- Alive now: 1073
- Gold now: 521
- HTTP: 409 alive / 160 gold
- HTTPS: 257 alive / 88 gold
- SOCKS4: 221 alive / 146 gold
- SOCKS5: 186 alive / 127 gold

## Historical pool

- Discovered: 123229
- Ever alive: 19003
- Ever gold: 730

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
