# SyndProxy validated proxy pool

## Current pool

- Alive now: 541
- Gold now: 373
- HTTP: 88 alive / 41 gold
- HTTPS: 45 alive / 11 gold
- SOCKS4: 199 alive / 159 gold
- SOCKS5: 209 alive / 162 gold

## Historical pool

- Discovered: 172322
- Ever alive: 32978
- Ever gold: 1220

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
