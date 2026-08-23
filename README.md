# SyndProxy validated proxy pool

## Current pool

- Alive now: 1269
- Gold now: 11
- HTTP: 615 alive / 10 gold
- HTTPS: 235 alive / 0 gold
- SOCKS4: 238 alive / 0 gold
- SOCKS5: 181 alive / 1 gold

## Historical pool

- Discovered: 169344
- Ever alive: 32654
- Ever gold: 1191

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
