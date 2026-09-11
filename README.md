# SyndProxy validated proxy pool

## Current pool

- Alive now: 520
- Gold now: 444
- HTTP: 111 alive / 84 gold
- HTTPS: 47 alive / 27 gold
- SOCKS4: 178 alive / 163 gold
- SOCKS5: 184 alive / 170 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49181
- Ever gold: 1575

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
