# SyndProxy private pool

## Current pool

- Alive now: 988
- Gold now: 385
- HTTP: 296 alive / 87 gold
- HTTPS: 216 alive / 28 gold
- SOCKS4: 233 alive / 123 gold
- SOCKS5: 243 alive / 147 gold

## Historical pool

- Discovered: 164181
- Ever alive: 32052
- Ever gold: 1170

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
