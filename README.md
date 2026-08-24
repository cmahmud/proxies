# SyndProxy validated proxy pool

## Current pool

- Alive now: 573
- Gold now: 437
- HTTP: 123 alive / 80 gold
- HTTPS: 88 alive / 25 gold
- SOCKS4: 172 alive / 161 gold
- SOCKS5: 190 alive / 171 gold

## Historical pool

- Discovered: 181856
- Ever alive: 34155
- Ever gold: 1253

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
