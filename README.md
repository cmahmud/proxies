# SyndProxy validated proxy pool

## Current pool

- Alive now: 521
- Gold now: 430
- HTTP: 113 alive / 82 gold
- HTTPS: 51 alive / 28 gold
- SOCKS4: 172 alive / 156 gold
- SOCKS5: 185 alive / 164 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49428
- Ever gold: 1583

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
