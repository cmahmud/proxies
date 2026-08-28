# SyndProxy validated proxy pool

## Current pool

- Alive now: 494
- Gold now: 389
- HTTP: 84 alive / 55 gold
- HTTPS: 70 alive / 15 gold
- SOCKS4: 168 alive / 161 gold
- SOCKS5: 172 alive / 158 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42893
- Ever gold: 1364

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
