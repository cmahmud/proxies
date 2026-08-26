# SyndProxy validated proxy pool

## Current pool

- Alive now: 663
- Gold now: 399
- HTTP: 143 alive / 76 gold
- HTTPS: 177 alive / 25 gold
- SOCKS4: 162 alive / 147 gold
- SOCKS5: 181 alive / 151 gold

## Historical pool

- Discovered: 190445
- Ever alive: 40068
- Ever gold: 1306

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
