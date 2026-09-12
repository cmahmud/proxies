# SyndProxy validated proxy pool

## Current pool

- Alive now: 520
- Gold now: 435
- HTTP: 112 alive / 84 gold
- HTTPS: 56 alive / 31 gold
- SOCKS4: 171 alive / 158 gold
- SOCKS5: 181 alive / 162 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49433
- Ever gold: 1583

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
