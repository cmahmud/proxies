# SyndProxy validated proxy pool

## Current pool

- Alive now: 561
- Gold now: 421
- HTTP: 105 alive / 63 gold
- HTTPS: 91 alive / 24 gold
- SOCKS4: 166 alive / 161 gold
- SOCKS5: 199 alive / 173 gold

## Historical pool

- Discovered: 183874
- Ever alive: 35760
- Ever gold: 1260

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
