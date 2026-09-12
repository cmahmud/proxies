# SyndProxy validated proxy pool

## Current pool

- Alive now: 556
- Gold now: 470
- HTTP: 134 alive / 100 gold
- HTTPS: 56 alive / 35 gold
- SOCKS4: 171 alive / 161 gold
- SOCKS5: 195 alive / 174 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49361
- Ever gold: 1579

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
