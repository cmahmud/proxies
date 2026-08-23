# SyndProxy validated proxy pool

## Current pool

- Alive now: 574
- Gold now: 306
- HTTP: 144 alive / 37 gold
- HTTPS: 57 alive / 10 gold
- SOCKS4: 192 alive / 152 gold
- SOCKS5: 181 alive / 107 gold

## Historical pool

- Discovered: 171039
- Ever alive: 32826
- Ever gold: 1212

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
