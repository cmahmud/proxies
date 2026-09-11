# SyndProxy validated proxy pool

## Current pool

- Alive now: 513
- Gold now: 434
- HTTP: 97 alive / 76 gold
- HTTPS: 53 alive / 25 gold
- SOCKS4: 181 alive / 163 gold
- SOCKS5: 182 alive / 170 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49140
- Ever gold: 1575

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
