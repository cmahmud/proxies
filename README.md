# SyndProxy validated proxy pool

## Current pool

- Alive now: 547
- Gold now: 469
- HTTP: 129 alive / 97 gold
- HTTPS: 47 alive / 32 gold
- SOCKS4: 177 alive / 162 gold
- SOCKS5: 194 alive / 178 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49416
- Ever gold: 1580

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
