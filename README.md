# SyndProxy validated proxy pool

## Current pool

- Alive now: 500
- Gold now: 393
- HTTP: 88 alive / 58 gold
- HTTPS: 49 alive / 9 gold
- SOCKS4: 172 alive / 160 gold
- SOCKS5: 191 alive / 166 gold

## Historical pool

- Discovered: 177985
- Ever alive: 33355
- Ever gold: 1234

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
