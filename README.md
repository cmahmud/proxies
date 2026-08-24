# SyndProxy validated proxy pool

## Current pool

- Alive now: 489
- Gold now: 393
- HTTP: 91 alive / 59 gold
- HTTPS: 36 alive / 13 gold
- SOCKS4: 171 alive / 158 gold
- SOCKS5: 191 alive / 163 gold

## Historical pool

- Discovered: 177985
- Ever alive: 33342
- Ever gold: 1234

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
