# SyndProxy validated proxy pool

## Current pool

- Alive now: 585
- Gold now: 440
- HTTP: 147 alive / 84 gold
- HTTPS: 81 alive / 23 gold
- SOCKS4: 169 alive / 161 gold
- SOCKS5: 188 alive / 172 gold

## Historical pool

- Discovered: 181494
- Ever alive: 33971
- Ever gold: 1253

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
