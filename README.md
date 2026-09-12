# SyndProxy validated proxy pool

## Current pool

- Alive now: 556
- Gold now: 471
- HTTP: 135 alive / 102 gold
- HTTPS: 56 alive / 34 gold
- SOCKS4: 174 alive / 161 gold
- SOCKS5: 191 alive / 174 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49359
- Ever gold: 1579

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
