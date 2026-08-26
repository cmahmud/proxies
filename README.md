# SyndProxy validated proxy pool

## Current pool

- Alive now: 673
- Gold now: 398
- HTTP: 144 alive / 78 gold
- HTTPS: 190 alive / 22 gold
- SOCKS4: 166 alive / 146 gold
- SOCKS5: 173 alive / 152 gold

## Historical pool

- Discovered: 190445
- Ever alive: 39954
- Ever gold: 1304

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
