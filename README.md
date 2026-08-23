# SyndProxy validated proxy pool

## Current pool

- Alive now: 529
- Gold now: 372
- HTTP: 86 alive / 40 gold
- HTTPS: 43 alive / 11 gold
- SOCKS4: 201 alive / 159 gold
- SOCKS5: 199 alive / 162 gold

## Historical pool

- Discovered: 172322
- Ever alive: 32978
- Ever gold: 1220

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
