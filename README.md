# SyndProxy validated proxy pool

## Current pool

- Alive now: 629
- Gold now: 334
- HTTP: 131 alive / 77 gold
- HTTPS: 91 alive / 30 gold
- SOCKS4: 97 alive / 53 gold
- SOCKS5: 310 alive / 174 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48559
- Ever gold: 1545

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
