# SyndProxy validated proxy pool

## Current pool

- Alive now: 505
- Gold now: 420
- HTTP: 97 alive / 73 gold
- HTTPS: 34 alive / 13 gold
- SOCKS4: 182 alive / 164 gold
- SOCKS5: 192 alive / 170 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48938
- Ever gold: 1569

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
