# SyndProxy validated proxy pool

## Current pool

- Alive now: 541
- Gold now: 467
- HTTP: 126 alive / 93 gold
- HTTPS: 50 alive / 37 gold
- SOCKS4: 178 alive / 162 gold
- SOCKS5: 187 alive / 175 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49402
- Ever gold: 1579

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
