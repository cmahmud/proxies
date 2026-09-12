# SyndProxy validated proxy pool

## Current pool

- Alive now: 520
- Gold now: 435
- HTTP: 111 alive / 84 gold
- HTTPS: 55 alive / 31 gold
- SOCKS4: 171 alive / 155 gold
- SOCKS5: 183 alive / 165 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49431
- Ever gold: 1583

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
