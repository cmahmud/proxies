# SyndProxy validated proxy pool

## Current pool

- Alive now: 883
- Gold now: 12
- HTTP: 436 alive / 10 gold
- HTTPS: 147 alive / 1 gold
- SOCKS4: 129 alive / 0 gold
- SOCKS5: 171 alive / 1 gold

## Historical pool

- Discovered: 169344
- Ever alive: 32654
- Ever gold: 1191

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
