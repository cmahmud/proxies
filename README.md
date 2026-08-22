# SyndProxy private pool

## Current pool

- Alive now: 823
- Gold now: 424
- HTTP: 238 alive / 93 gold
- HTTPS: 169 alive / 26 gold
- SOCKS4: 190 alive / 147 gold
- SOCKS5: 226 alive / 158 gold

## Historical pool

- Discovered: 162754
- Ever alive: 31567
- Ever gold: 1161

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
