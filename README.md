# SyndProxy validated proxy pool

## Current pool

- Alive now: 523
- Gold now: 402
- HTTP: 91 alive / 60 gold
- HTTPS: 76 alive / 19 gold
- SOCKS4: 169 alive / 157 gold
- SOCKS5: 187 alive / 166 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38520
- Ever gold: 1290

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
