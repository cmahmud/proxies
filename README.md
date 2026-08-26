# SyndProxy validated proxy pool

## Current pool

- Alive now: 638
- Gold now: 390
- HTTP: 123 alive / 69 gold
- HTTPS: 172 alive / 25 gold
- SOCKS4: 162 alive / 146 gold
- SOCKS5: 181 alive / 150 gold

## Historical pool

- Discovered: 190445
- Ever alive: 39826
- Ever gold: 1304

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
