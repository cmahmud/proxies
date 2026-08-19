# SyndProxy private pool

## Current pool

- Alive now: 1029
- Gold now: 520
- HTTP: 362 alive / 158 gold
- HTTPS: 247 alive / 90 gold
- SOCKS4: 216 alive / 150 gold
- SOCKS5: 204 alive / 122 gold

## Historical pool

- Discovered: 123229
- Ever alive: 18998
- Ever gold: 730

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
