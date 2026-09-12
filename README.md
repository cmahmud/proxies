# SyndProxy validated proxy pool

## Current pool

- Alive now: 470
- Gold now: 418
- HTTP: 97 alive / 73 gold
- HTTPS: 41 alive / 25 gold
- SOCKS4: 161 alive / 158 gold
- SOCKS5: 171 alive / 162 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49456
- Ever gold: 1583

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
