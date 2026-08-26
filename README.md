# SyndProxy validated proxy pool

## Current pool

- Alive now: 474
- Gold now: 399
- HTTP: 86 alive / 59 gold
- HTTPS: 33 alive / 14 gold
- SOCKS4: 171 alive / 162 gold
- SOCKS5: 184 alive / 164 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38978
- Ever gold: 1295

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
