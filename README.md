# SyndProxy validated proxy pool

## Current pool

- Alive now: 556
- Gold now: 471
- HTTP: 132 alive / 99 gold
- HTTPS: 58 alive / 36 gold
- SOCKS4: 174 alive / 163 gold
- SOCKS5: 192 alive / 173 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49362
- Ever gold: 1579

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
