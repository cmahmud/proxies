# SyndProxy validated proxy pool

## Current pool

- Alive now: 466
- Gold now: 414
- HTTP: 82 alive / 64 gold
- HTTPS: 37 alive / 22 gold
- SOCKS4: 166 alive / 156 gold
- SOCKS5: 181 alive / 172 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48826
- Ever gold: 1567

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
