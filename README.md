# SyndProxy validated proxy pool

## Current pool

- Alive now: 533
- Gold now: 404
- HTTP: 115 alive / 67 gold
- HTTPS: 54 alive / 13 gold
- SOCKS4: 173 alive / 159 gold
- SOCKS5: 191 alive / 165 gold

## Historical pool

- Discovered: 177985
- Ever alive: 33329
- Ever gold: 1234

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
