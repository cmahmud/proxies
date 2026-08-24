# SyndProxy validated proxy pool

## Current pool

- Alive now: 595
- Gold now: 435
- HTTP: 135 alive / 84 gold
- HTTPS: 93 alive / 19 gold
- SOCKS4: 176 alive / 161 gold
- SOCKS5: 191 alive / 171 gold

## Historical pool

- Discovered: 181856
- Ever alive: 34433
- Ever gold: 1255

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
