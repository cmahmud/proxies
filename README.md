# SyndProxy validated proxy pool

## Current pool

- Alive now: 498
- Gold now: 425
- HTTP: 97 alive / 75 gold
- HTTPS: 30 alive / 14 gold
- SOCKS4: 182 alive / 164 gold
- SOCKS5: 189 alive / 172 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48934
- Ever gold: 1569

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
